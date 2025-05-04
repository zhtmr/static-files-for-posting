# static-files-for-posting
블로그 포스팅에 쓰일 파일 저장소   
🔗 https://zhtmr.github.io/static-files-for-posting/


> [!NOTE]  
> url 주소 github pages 로 변경!
> - `https://zhtmr.github.io/static-files-for-posting/images/폴더/파일명`
> - ex : `https://zhtmr.github.io/static-files-for-posting/images/20240917/img_3.png`


- GitHub 저장소에 올린 이미지들을 웹에서 볼 수 있도록 `index.html` 생성
- Push 전에 Python 스크립트를 이용해 자동으로 목록 업데이트
- 필요 시 Git Hook을 이용한 반자동화

## 사용방법
```bash
python generate_index.py
git add images/ index.html
git commit -m "Add images and update index"
git push
```

## Git Hook 으로 반자동화
커밋 전에 자동으로 index.html을 생성하려면 .git/hooks/pre-commit에 아래 스크립트 작성
```bash
#!/bin/bash
python generate_index.py
git add index.html
```

실행 권한 부여
```bash
chmod +x .git/hooks/pre-commit
```

