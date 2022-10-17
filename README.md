# Generate Chia NFT metadata

## Setup (quick)
1. Run `pip install -r requirements.txt`

## Setup (complete)
1. You don't need above if you don't care about JSON schema validation
1. Otherwise you can also use virtual environment to keep everything sandboxed to this project:
    
  ```
  python3 -m venv nftvenv
  . nftvenv/bin/activate
  pip install -r requirements.txt
  . nftvenv/bin/activate
  ```
    
1. In the future you should only need to activate the `venv` via: `. nftvenv/bin/activate`


## Usage

#### Generate UUID:

`python metadata.py -gu`

#### Generate a single NFT metadata file (output defaultst to: `_output`):

`python metadata.py -cm collection_metadata.json -gm "1" "Friendly Marmots #0001" "Eco friendly avatars" '{"Head":"yes", "Body":"wow", "Eyes":3}'`

#### Generate a single NFT metadata file (custom output dir):

`python metadata.py -cm collection_metadata.json -od "_meta" -gm "1" "Friendly Marmots #0001" "Eco friendly avatars" '{"Head":"yes", "Body":"wow", "Eyes":3}'`

#### Validate JSON schema (defaults to using Chia CHIP-0007 NFT1 schema):

`python metadata.py -vm "_meta"`

## How-To

1. Generate the your collection UUID (do this only one time per NFT collection): `python metadata.py -gu`
1. Copy the `collection_metadata.json` and rename to `<your-project-name>-collection-metadata.json` (i.e. `friendly-marmots-collection-metadata.json`)
  * Edit the collection metadata file
  * Change the UUID
  * Update project relevant descriptions, URLs and social media handles.
1. Generate a single metadata file with any attributes (see `-gm` command above)
1. Copy/paste the output to [https://www.jsonschemavalidator.net/s/0Aw7Bmlb](https://www.jsonschemavalidator.net/s/0Aw7Bmlb) to validate ouput.
1. You are now ready to upload to IPFS/Arweave.

## Output

Output will go into `_output/1.json`:

```
{
    "format": "CHIP-0007",
    "name": "Friendly Marmots #0001",
    "description": "Eco friendly avatars",
    "sensitive_content": false,
    "attributes": [
        {
            "trait_type": "Generation",
            "value": 1
        },
        {
            "trait_type": "Head",
            "value": "yes"
        },
        {
            "trait_type": "Body",
            "value": "wow"
        },
        {
            "trait_type": "Eyes",
            "value": "3"
        }
    ],
    "collection": {
        "name": "NFT Name",
        "id": "ACA68789-1BE5-431F-9441-BD3EB09116E6",
        "attributes": [
            {
                "type": "description",
                "value": "Example collection of 10000 unique marmots."
            },
            {
                "type": "icon",
                "value": "https://nftexample.com/assets/img/thumbnail.png"
            },
            {
                "type": "banner",
                "value": "https://nftexample.com/assets/img/banner.png"
            },
            {
                "type": "twitter",
                "value": "@NFTexample"
            },
            {
                "type": "website",
                "value": "https://nftexample.com"
            }
        ]
    }
}
```
## Requirements

Python 3.6+

## Known Issues

1. Attributes passed in as integers get converted to string literals.