import json
import asyncio
import os
import argparse
import sys
import uuid

# validation
import pathlib
import jsonschema

########################################################################

##   Replace the values in collection_metadata.json before starting   ##

########################################################################

# Replace if needed
OUTPUT_DIR="_output"
CHIP0007_SCHEMA_PATH="CHIP-0007-NFT1-JSON-SCHEMA.json"

def gen_chia_chip_0007_attributes_from_json(key_value_json):
    chip0007_formatted_json = []
    
    try:
        # load the JSON string
        json_data = json.loads(key_value_json)
    except Exception as e:
        print(e)
        sys.exit(f"ERROR parsing JSON: {key_value_json}")
    
    for attribute in json_data:
        # print(attribute + ":" + json_data[attribute])
        key = attribute
        value = json_data[attribute]
        json_attribute = {
          "trait_type": f"{key}",
          "value": value
        }
        chip0007_formatted_json.append(json_attribute)
    
    return chip0007_formatted_json

def gen_nft_metadata(nft_number, nft_name, nft_description, output_dir, first_trait_value, collection_metadata_path):
    
    if os.path.exists(collection_metadata_path) != True:
        sys.exit(f"ERROR collection metadata not found in {cpath}")
    
    meta = {
      "format": "CHIP-0007",
      "minting_tool": "scotopic",
      "name": f"{nft_name}",
      "description": f"{nft_description}",
      "sensitive_content": False,
      "attributes": [
        {
          "trait_type": "Generation",
          "value": 1
        }
      ]
    }
    
    with open(collection_metadata_path, 'r') as f:
      collection_metadata = json.load(f)
      # collection_metadata = json.dumps(collection_metadata_dict, indent=2, sort_keys=False)
    
    meta["collection"] = collection_metadata["collection"]
    
    extra_attributes = gen_chia_chip_0007_attributes_from_json(first_trait_value)
    
    if len(extra_attributes) > 0:
        for attr in extra_attributes:
            meta["attributes"].append(attr)
    
    fname = f"{nft_number}.json"
    
    try:
        if os.path.exists(output_dir) != True:
            os.mkdir(output_dir)
    except Exception as e:
        print(e)
        sys.exit(f"ERROR creating {output_dir}")
    
    try:
        with open(f"{output_dir}/" + fname, 'w', encoding='utf8') as outfile:
            json.dump(meta, outfile, sort_keys=False, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)
        sys.exit(f"ERROR writing out {fname}")
        

def validate_nft_metadata(metadata_dir, json_schema_path):
    # Example of validation https://www.jsonschemavalidator.net/s/0Aw7Bmlb
    
    if os.path.exists(metadata_dir) != True:
        sys.exit(f"ERROR metadata dir not found in {metadata_dir}")
    if os.path.exists(json_schema_path) != True:
        sys.exit(f"ERROR: CHIP JSON schema not found: {json_schema_path}")
    
    print(f"Validating JSON schema in: {metadata_dir}")
    
    with open(json_schema_path, 'r') as f:
      json_schema = json.load(f)
    
    dir_enumerator = os.listdir(metadata_dir)
    dirs_sorted = sorted(dir_enumerator)
    is_unclean_dir = False
    
    for count, filename in enumerate(dirs_sorted):
        
        path = os.path.join(metadata_dir, filename)
        
        file_extension = pathlib.Path(filename).suffix
        
        if file_extension != ".json":
            is_unclean_dir = True
            continue
        
        try:
            with open(path, 'r') as f:
              json_data = json.load(f)
        except Exception as e:
            print(e)
            sys.exit(f"ERROR reading {path}")
        
        try:
            jsonschema.validate(instance=json_data, schema=json_schema)
        except jsonschema.exceptions.ValidationError as err:
            print("Invalid schema foudn:")
            sys.exit(err)
    
    if is_unclean_dir == True:
        print("WARNING: found non .json files that were ignored")
    
    print("SUCCESS: all json was valid")
    
def generate_uuid():
    print(str(uuid.uuid4()).upper())

def get_args():
    
    parser = argparse.ArgumentParser(description='Generate valid Chia CHIP-0007 metadata.')
    
    ## Generate UUID for hte project
    parser.add_argument('-gu', '--generate-uuid', action='store_true', required=False, help='Generate a new Chia NFT collection UUID.')
    
    ## Generate Chia CHIP-0007 NFT1 metadata
    parser.add_argument('-cm', '--collection-metadata-path', metavar=('COLLECTION_METADATA_PATH'), nargs=1, required=False, help='Metadata YAML file for your collection.')
    parser.add_argument('-gm', '--generate-metadata', metavar=('NFT_NUMBER', 'NFT_NAME', 'NFT_DESCRIPTION', 'TRAITS_AS_KEY_VALUE_JSON'), nargs=4, required=False, help='Generate NFT metadata.\nExample: python metadata.py -gm "0001" "Eco Friends #0001" "The one that got away" "{"Body":"K33", "Eyes":3, "Mouth":"Nasty"}"')
    parser.add_argument('-od', '--output-dir', metavar=('OUTPUT_DIR'), nargs=1, required=False, help='Custom output directory that overwrites the default')
    
    ## Validate Chia CHIP-0007 NFT1 metadata (or specify a path to your own schema)
    parser.add_argument('-vm', '--validate-metadata', metavar=('METADATA_DIR'), nargs=1, required=False, help='Parse all JSON files in this dir and validate each file.')
    parser.add_argument('-vs', '--validation-schema-path', metavar=('JSON_SCHEMA_PATH'), nargs=1, required=False, help='Path to a JSON schema file.')
    
    if len(sys.argv) < 2:
        # parser.print_usage()
        parser.print_help()
        sys.exit(1)
    
    return parser.parse_args()

async def main():
    
    ARGS = get_args()
    
    output_dir = OUTPUT_DIR
    if ARGS.output_dir:
        output_dir = ARGS.output_dir[0]
    
    json_schema_file_path = CHIP0007_SCHEMA_PATH
    if ARGS.validation_schema_path:
        json_schema_file_path = ARGS.validation_schema_path[0]
    
    if ARGS.collection_metadata_path:
        collection_metadata_path = ARGS.collection_metadata_path[0]
    
    if ARGS.generate_metadata:
        if os.path.exists(collection_metadata_path) != True:
            sys.exit(f"ERROR collection metadata not found in {collection_metadata_path}")
        
        nft_number = ARGS.generate_metadata[0]
        nft_name = ARGS.generate_metadata[1]
        nft_description = ARGS.generate_metadata[2]
        traits_as_key_values_json_string = ARGS.generate_metadata[3]
        gen_nft_metadata(nft_number, nft_name, nft_description, output_dir, traits_as_key_values_json_string, collection_metadata_path)
    elif ARGS.validate_metadata:
        metadata_dir = ARGS.validate_metadata[0]
        validate_nft_metadata(metadata_dir, json_schema_file_path)
    elif ARGS.generate_uuid:
        generate_uuid()
    

# Prevent auto executing main when called from another program
if __name__ == "__main__":
    asyncio.run(main())

