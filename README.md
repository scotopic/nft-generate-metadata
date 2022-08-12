# Generate Chia NFT metadata

## Usage

Generate UUID:
`python metadata.py -gu`

Generate a single NFT metadata file:
`python metadata.py -gm "1" "Friendly Marmots #0001" "Eco friendly avatars" '{"Head":"yes", "Body":"wow", "Eyes":3}'`

## Usage

1. Generate the your collection UUID (do this only one time per NFT collection): `python metadata.py -gu`
1. Open `metadata.py` and replace the your specific collection related info
1. Generate a single metadata file with any attributes: `python metadata.py -gm "1" "Friendly Marmots #0001" "Eco friendly avatars" '{"Head":"yes", "Body":"wow", "Eyes":3}'`
1. Copy/paste the output to [https://www.jsonschemavalidator.net/s/0Aw7Bmlb](https://www.jsonschemavalidator.net/s/0Aw7Bmlb) to validate ouput.
1. You are now ready to upload to IPFS/Arweave.

## Output

Output will go into `_output/1.json`:
```
{
    "format": "CHIP-0007",
    "name": "Chia Friends #0001",
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