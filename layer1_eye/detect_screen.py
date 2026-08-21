from pathlib import Path
import cv2


BASE_DIR = Path(__file__).resolve().parent
INPUT_IMAGE = BASE_DIR / "last_capture.png"
OUTPUT_IMAGE = BASE_DIR / "detected_screen.png"


def detect_screen(image):
    """
    Detect the largest rectangular screen-like region
    using Canny edge detection and contours.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce small noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    best_contour = None
    best_area = 0

    image_area = image.shape[0] * image.shape[1]

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore very small regions
        if area < image_area * 0.10:
            continue

        perimeter = cv2.arcLength(contour, True)

        if perimeter == 0:
            continue

        approximation = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True
        )

        # A screen is approximately rectangular
        if len(approximation) == 4 and area > best_area:
            best_contour = approximation
            best_area = area

    # If no rectangle is detected, use the complete image
    if best_contour is None:
        print("[Layer 1.2] No rectangular screen detected.")
        print("[Layer 1.2] Using complete image as fallback.")

        return image, None

    x, y, w, h = cv2.boundingRect(best_contour)

    cropped = image[y:y + h, x:x + w]

    print("[Layer 1.2] Screen detected.")
    print(f"[Layer 1.2] Position: x={x}, y={y}")
    print(f"[Layer 1.2] Size: width={w}, height={h}")
    print(f"[Layer 1.2] Area: {best_area:.0f} pixels")

    return cropped, (x, y, w, h)


if __name__ == "__main__":

    if not INPUT_IMAGE.exists():
        raise FileNotFoundError(
            f"Input image not found: {INPUT_IMAGE}"
        )

    image = cv2.imread(str(INPUT_IMAGE))

    if image is None:
        raise RuntimeError(
            f"Unable to read image: {INPUT_IMAGE}"
        )

    screen, coordinates = detect_screen(image)

    success = cv2.imwrite(
        str(OUTPUT_IMAGE),
        screen
    )

    if not success:
        raise RuntimeError(
            "Failed to save detected screen image."
        )

    print(f"[Layer 1.2] Output saved to: {OUTPUT_IMAGE}")