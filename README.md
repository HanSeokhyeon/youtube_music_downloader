# 유튜브 음악 자동 다운로더

.txt나 .csv로 작성된 유투브 링크들을 자동으로 다운로드하는 코드입니다. (웹 개발 예정)

## 설치

2가지 프로그램과 파이썬 numpy 패키지가 필요합니다.

### 1. youtube-dl

Ubuntu
```bash
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

macOS
```bash
brew install youtube-dl
```

### 2. ffmpeg

Ubuntu
```bash
sudo apt install ffmpeg
```

macOS
```bash
brew install ffmpeg
```

### 3. numpy
```bash
pip install numpy
```

## 사용

### 1. 링크 파일 준비
```csv
크러쉬,OASIS,https://www.youtube.com/watch?v=fE2h3lGlOsk
적재,잘지내,https://www.youtube.com/watch?v=zndvqTc4P9I
...
```
위와 같은 양식으로 링크들을 넣어주면 됩니다. 파일 확장자는 csv나 txt로 작성하면 됩니다.

### 2. 실행
```bash
python downloader.py <link file path>

ex) python downloader.py test.csv
```

## Docker로 실행

```bash
docker run -v <project directory>:/opt/project hsh0322/youtube-dl python downloader.py <link file path>

ex) docker run -v ~/youtube_music_downloader:/opt/project hsh0322/youtube-dl python downloader.py test.csv
```
