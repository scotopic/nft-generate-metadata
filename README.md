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

## Requirements

Python 3.6+

## Known Issues

1. Attributes passed in as integers get converted to string literals.