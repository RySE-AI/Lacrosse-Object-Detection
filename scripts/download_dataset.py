from argparse import ArgumentParser
from roboflow import Roboflow


def load_dataset_from_roboflow(args) -> None:
    save_dir = f"{args.save_destination}/version_{args.version}"
    rf = Roboflow(api_key=args.api_key)
    project = rf.workspace("ryseai").project("lacrosse-object-detection")
    _ = project.version(args.version).download(
        args.format, location=save_dir
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-api",
        "--api-key",
        help="Specify your api key from roboflow",
        required=True,
        type=str,
    )

    parser.add_argument(
        "-v",
        "--version",
        required=True,
        help="Specify the dataset version with a number",
        type=int,
    )

    parser.add_argument(
        "-d",
        "--save-destination",
        help="Download Destination",
        default="./",
        type=str
    )

    parser.add_argument(
        "-f",
        "--format",
        help="Specify annotation format",
        type=str
    )

    args = parser.parse_args()
    load_dataset_from_roboflow(args)
