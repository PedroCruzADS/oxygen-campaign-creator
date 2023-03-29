import os
from facebook_business.adobjects.adimage import AdImage


def create_hash_images(image_files: dict, path: str, ad_account_id: str):
    files = []
    for file in image_files:
        image = image_files[file]
        image_path = os.path.join(path, image.filename)
        files.append(image_path)
        image.save(image_path)
        print(image_path)

    hash_files = []
    for f in files:
        image = AdImage(parent_id=ad_account_id)
        image[AdImage.Field.filename] = f
        image.remote_create()
        image_hash = image[AdImage.Field.hash]
        hash_files.append(image_hash)

    return hash_files