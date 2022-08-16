import json
import asyncio
import os
import argparse
import sys
import uuid

##############################
#### REPLACE THESE VALUES ####
##############################
NFT_COLLECTION_UUID="Run <python metadata.py -gu>"
NFT_COLLECTION_NAME="Collection Name"
NFT_COLLECTION_DESCRIPTION="Example collection of 10000 unique marmots."
NFT_COLLECTION_ICON_URI="https://nftexample.com/assets/img/thumbnail.png"
NFT_COLLECTION_BANNER_URI="https://nftexample.com/assets/img/banner.png"
NFT_COLLECTION_TWITTER_HANDLE="@NFTexample"
NFT_COLLECTION_WEBSITE_URI="https://nftexample.com"
##############################
#### REPLACE THESE VALUES ####
##############################

# Replace if needed
OUTPUT_DIR="_output"

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
          "value": f"{value}"
        }
        chip0007_formatted_json.append(json_attribute)
    
    return chip0007_formatted_json

def gen_nft_metadata(nft_number, nft_name, nft_description, output_dir, first_trait_value):
    
    meta = {
      "format": "CHIP-0007",
      "name": f"{nft_name}",
      "description": f"{nft_description}",
      "sensitive_content": False,
      "attributes": [
        {
          "trait_type": "Generation",
          "value": 1
        }
      ],
      "collection": {
        "name": f"{NFT_COLLECTION_NAME}",
        "id": f"{NFT_COLLECTION_UUID}",
        "attributes": [
          {
            "type": "description",
            "value": f"{NFT_COLLECTION_DESCRIPTION}"
          },
          {
              "type": "icon",
              "value": f"{NFT_COLLECTION_ICON_URI}"
          },
          {
              "type": "banner",
              "value": f"{NFT_COLLECTION_BANNER_URI}"
          },
          {
            "type": "twitter",
            "value": f"{NFT_COLLECTION_TWITTER_HANDLE}"
          },
          {
            "type": "website",
            "value": f"{NFT_COLLECTION_WEBSITE_URI}"
          }
        ]
      }
    }
    
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
        with open(f"{output_dir}/" + fname, 'w') as outfile:
            json.dump(meta, outfile, sort_keys=False, indent=4)
    except Exception as e:
        print(e)
        sys.exit(f"ERROR writing out {fname}")
        

def gen_nft_metadata_validate(nft_metadata_path):
    # https://www.jsonschemavalidator.net/s/0Aw7Bmlb
    print("do this")

def generate_uuid():
    print(str(uuid.uuid4()).upper())

def get_args():
    
    parser = argparse.ArgumentParser(description='Generate valid Chia CHIP-0007 metadata.')
    
    parser.add_argument('-gu', '--generate-uuid', action='store_true', required=False, help='Generate a new Chia NFT collection UUID.')
    parser.add_argument('-gm', '--generate-metadata', metavar=('NFT_NUMBER', 'NFT_NAME', 'NFT_DESCRIPTION', 'TRAITS_AS_KEY_VALUE_JSON'), nargs=4, required=False, help='Generate NFT metadata.\nExample: python metadata.py -gm "0001" "Eco Friends #0001" "The one that got away" "{"Body":"K33", "Eyes":3, "Mouth":"Nasty"}"')
    parser.add_argument('-od', '--output-dir', metavar=('OUTPUT_DIR'), nargs=1, required=False, help='Custom output directory that overwrites the default')
    
    if len(sys.argv) < 2:
        # parser.print_usage()
        parser.print_help()
        sys.exit(1)
    
    return parser.parse_args()

ARGS = get_args()

async def main():
    
    output_dir = OUTPUT_DIR
    if ARGS.output_dir:
        output_dir = ARGS.output_dir[0]
    
    
    if ARGS.generate_metadata:
        nft_number = ARGS.generate_metadata[0]
        nft_name = ARGS.generate_metadata[1]
        nft_description = ARGS.generate_metadata[2]
        traits_as_key_values_json_string = ARGS.generate_metadata[3]
        gen_nft_metadata(nft_number, nft_name, nft_description, output_dir, traits_as_key_values_json_string)
    elif ARGS.generate_uuid:
        generate_uuid()
    

asyncio.run(main())