import os

allowable_extensions = ["jpg", "jpeg", "png"]


def collect_img_paths(img_dir: str) -> list:
    try:
        print("STARTING: collect_img_paths")

        all_img_paths = [os.path.join(img_dir, name) for name in os.listdir(img_dir) if name.split(".")[-1] in allowable_extensions]
        all_img_paths = sorted(all_img_paths)
        all_img_paths = ["./data/input/" + v.split("/")[-1] for v in all_img_paths]

        print(f"SUCCESS: collect_img_paths ran successfully - image paths loaded from '{img_dir}'")
        return all_img_paths
    except Exception as e:
        print(f"FAILURE: collect_img_paths failed with img_dir {img_dir} with exception {e}")
        raise e
