import os

BASE_URL = "https://zhtmr.github.io/static-files-for-posting"

image_root = "images"
output_file = "index.html"
image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")

dates = sorted([
    d for d in os.listdir(image_root)
    if os.path.isdir(os.path.join(image_root, d))
])

with open(output_file, "w", encoding="utf-8") as f:
    f.write("""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>날짜별 이미지 보기</title>
  <style>
    body { font-family: sans-serif; padding: 1rem; background: #f4f4f4; }
    .date-button { cursor: pointer; padding: 0.5rem; margin: 0.25rem; background: #eee; border: 1px solid #ccc; display: inline-block; }
    .date-button:hover { background: #ddd; }
    .image-container { margin-top: 1rem; display: none; }
    img { max-width: 300px; display: block; margin-bottom: 0.5rem; }
    .path { font-size: 0.9em; background: #fff; padding: 0.3rem; border: 1px solid #ccc; word-break: break-all; }
  </style>
</head>
<body>
  <h1>날짜별 이미지 인덱스</h1>
""")

    for date in dates:
        folder = os.path.join(image_root, date)
        images = [img for img in os.listdir(folder) if img.lower().endswith(image_extensions)]
        if not images:
            continue

        f.write(f"<div class='date-button' onclick=\"toggle('{date}')\">📅 {date}</div>\n")
        f.write(f"<div id='{date}' class='image-container'>\n")

        for img in images:
            img_path = f"{image_root}/{date}/{img}"
            full_url = f"{BASE_URL}/{img_path}"
            f.write(f"<img src='{img_path}' alt='{img}' />\n")
            f.write(f"<div class='path'>{full_url}</div>\n")

        f.write("</div>\n")

    # 스크립트: 토글 기능
    f.write("""
<script>
  function toggle(id) {
    const el = document.getElementById(id);
    el.style.display = (el.style.display === "none" || el.style.display === "") ? "block" : "none";
  }
</script>
</body>
</html>
""")
