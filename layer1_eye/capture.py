from pathlib import Path
import cv2


BASE_DIR = Path(__file__).resolve().parent
TEST_IMAGE = BASE_DIR / "test_images" / "sample_monitor.png"
LAST_CAPTURE = BASE_DIR / "last_capture.png"


def get_frame(source="webcam"):
    """
    Capture one frame from the webcam.

    If source='test_image', load the bundled test image.
    If the webcam is unavailable, automatically use the test image.
    """

    # Test-image mode
    if source == "test_image":
        image = cv2.imread(str(TEST_IMAGE))

        if image is None:
            raise FileNotFoundError(
                f"Test image not found: {TEST_IMAGE}"
            )

        return image

    # Webcam mode
    camera = cv2.VideoCapture(0)

    if camera.isOpened():
        success, frame = camera.read()
        camera.release()

        if success and frame is not None:
            return frame

    camera.release()

    print(
        "[Layer 1.1] Webcam unavailable. "
        "Falling back to test image."
    )

    return get_frame(source="test_image")


if __name__ == "__main__":

    frame = get_frame()

    cv2.imwrite(str(LAST_CAPTURE), frame)

    print(f"Capture successful.")
    print(f"Saved to: {LAST_CAPTURE}")
    print(f"Image size: {frame.shape}")