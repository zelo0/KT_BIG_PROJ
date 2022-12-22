const video = document.getElementById("video");

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri("/static/models"),
  faceapi.nets.faceLandmark68Net.loadFromUri("/static/models"),
  faceapi.nets.faceRecognitionNet.loadFromUri("/static/models"),
  faceapi.nets.faceExpressionNet.loadFromUri("/static/models"),
]).then(startVideo);

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    (stream) => (video.srcObject = stream),
    (err) => console.error(err)
  );
}

video.addEventListener("play", () => {
  const canvas = faceapi.createCanvasFromMedia(video);
  canvas.id = "match-dimension";
  document.body.append(canvas);

  const displaySize = { width: video.width, height: video.height };
  faceapi.matchDimensions(canvas, displaySize);

  setInterval(async () => {
    const detections = await faceapi
      .detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks();
    // .withFaceExpressions(); // 주석
    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
    // faceapi.draw.drawDetections(canvas, resizedDetections); // 주석
    // faceapi.draw.drawFaceLandmarks(canvas, resizedDetections); // 주석
    // faceapi.draw.drawFaceExpressions(canvas, resizedDetections); // 주석

    // const test3 = resizedDetections[0].landmarks._positions.map(e => e._x);
    // const test4 = resizedDetections[0].landmarks._positions.map(r => r._y);

    try {
      const test3 = resizedDetections[0].landmarks._positions; // 예외 발생
      // console.log(test3, test4)
      // localStorage.car = JSON.stringify(test3);
      const jsonData = JSON.stringify(test3);
      // console.log(jsonData); // 확인해보니 그림은 크게 나오지만 좌표에는 이상 없음

      function saveAsFile(str, filename) {
        var hiddenElement = document.createElement("a");
        hiddenElement.href = "data:attachment/text," + encodeURI(str);
        hiddenElement.target = "_blank";
        hiddenElement.download = filename;
        hiddenElement.click();
      }
    } catch (e) {
      const warningText = this.add.text(300, 300, "miss"); // 미완성
    }

    // saveAsFile(jsonData, "output.json");
  }, 100); // 현재 0.1초
});
