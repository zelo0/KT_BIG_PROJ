var distance_array = [];
var count = 0;
var count2 = 0;
var mouth_skill_count = 1;
var left_skill_count = 1;
var right_skill_count = 1;
let left_count2 = 0;
let right_count2 = 0;
var time_delay = 0;
const getElNum = (arr, el) => arr.reduce((ac, v) => ac + (v === el), 0);
x_arr = [];
y_arr = [];

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
    canvas.getContext("2d").clearRect(0, 0, video.width, video.height);

    ///////////// 새로 추가
    let context = canvas.getContext("2d");
    let src = new cv.Mat(video.height, video.width, cv.CV_8UC4);
    let dst = new cv.Mat(video.height, video.width, cv.CV_8UC1);
    //context.drawImage(video, 0, 0, video.width, video.height);
    src.data.set(context.getImageData(0, 0, video.width, video.height).data);
    // faceapi.draw.drawDetections(canvas, resizedDetections); // 주석
    // faceapi.draw.drawFaceLandmarks(canvas, resizedDetections); // 주석
    // faceapi.draw.drawFaceExpressions(canvas, resizedDetections); // 주석

    // x, y 좌표 어레이 생성
    let test_x = resizedDetections[0].landmarks._positions.map((e) => e._x);
    let test_y = resizedDetections[0].landmarks._positions.map((e) => e._y);

    x_arr.push(test_x);
    y_arr.push(test_x);

    // cv.cvtColor(src, dst, cv.COLOR_RGBA2GRAY);
    // 눈을 감았는지 떴는지를 opencv로 확인

    // cvtGray()
    // let src = new cv.Mat(canvas.height, canvas.width, cv.CV_8UC4);

    // let ctx = textToImg.getContext('2d');
    // let imgData = ctx.getImageData(0, 0, 720, 560);

    // let src = cv.matFromImageData(imgData);

    let x_left = (30 - (test_x[39] - test_x[36])) / 2;
    let x_right = (30 - (test_x[45] - test_x[42])) / 2;
    let y_left = (20 - (test_y[40] - test_y[37])) / 2;
    let y_right = (20 - (test_y[47] - test_y[43])) / 2;

    let x_df_eye_left_start = parseInt(test_x[36] - x_left);
    let x_df_eye_left_end = 30;
    // let x_df_eye_left_end = parseInt(test_x[39] + x_left) - x_df_eye_left_start

    let y_df_eye_left_start = parseInt(test_y[38] - y_left);
    let y_df_eye_left_end = 20;

    let x_df_eye_right_start = parseInt(test_x[42] - x_right);
    let x_df_eye_right_end = 30;

    let y_df_eye_right_start = parseInt(test_y[44] - y_right);
    let y_df_eye_right_end = 20;

    // You can try more different parameters
    let rect_left = new cv.Rect(
      x_df_eye_left_start,
      y_df_eye_left_start,
      x_df_eye_left_end,
      y_df_eye_left_end
    );
    dst_left = src.roi(rect_left);

    let rect_right = new cv.Rect(
      x_df_eye_right_start,
      y_df_eye_right_start,
      x_df_eye_right_end,
      y_df_eye_right_end
    );
    dst_right = src.roi(rect_right);

    cv.cvtColor(dst_left, dst_left, cv.COLOR_RGBA2GRAY);
    cv.cvtColor(dst_right, dst_right, cv.COLOR_RGBA2GRAY);

    cv.threshold(dst_left, dst, 0, 255, cv.THRESH_OTSU);
    let left_array = JSON.parse("[" + dst.data.toString() + "]");

    cv.threshold(dst_right, dst, 0, 255, cv.THRESH_OTSU);
    let right_array = JSON.parse("[" + dst.data.toString() + "]");

    let left_matrix = listToMatrix(left_array, 30);
    let right_matrix = listToMatrix(right_array, 30);

    let left_count = 0;
    let right_count = 0;
    let left_count_check;
    let right_count_check;

    for (var i = 12; i <= 20; i++) {
      if (Array.isArray(right_matrix[i])) {
        right_count_check = getElNum(right_matrix[i], 255);
      }

      if (right_count_check < 20) {
        // console.log('왼쪽 눈을 감음')
        right_count++;
      } else {
        // console.log('왼쪽 눈을 뜸')
        right_count2 = 0;
      }
      if (Array.isArray(left_matrix[i])) {
        left_count_check = getElNum(left_matrix[i], 255);
      }

      if (left_count_check < 10) {
        // console.log('오른쪽 눈을 감음')
        left_count++;
      } else {
        // console.log('오른쪽 눈을 뜸')
        left_count2 = 0;
      }
    }
    //console.log("눈 감은 횟수", left_count_check, right_count_check);
    if (left_count >= 8 && left_count2 == 0) {
      attackAction();
      console.log("오른쪽 눈 스킬발동" + String(left_skill_count) + "번!");
      left_count = 0;
      left_count2++;
      left_skill_count++;
    }

    if (right_count >= 8 && right_count2 == 0) {
      attackAction();
      console.log("왼쪽 눈 스킬발동" + String(right_skill_count) + "번!");
      right_count = 0;
      right_count2++;
      right_skill_count++;
    }

    src.delete();
    dst.delete();
    dst_left.delete();
    dst_right.delete();

    // 입벌림을 감지하는 부분
    let test_x_29 = test_x[29];
    let test_x_57 = test_x[57];

    let test_y_29 = test_y[29];
    let test_y_57 = test_y[57];

    let x_sub = test_x_57 - test_x_29;
    let y_sub = test_y_57 - test_y_29;

    let distance = (x_sub ** 2 + y_sub ** 2) ** (1 / 2);

    distance_array.push(distance);

    if (distance >= distance_array[0] * 1.35) {
      // console.log( " 입벌림 " );
      count++;
    } else {
      // console.log( " 입닫음 " );
      count = 0;
      count2 = 0;
    }
    if (count == 1 && count2 == 0) {
      attackAction();
      console.log("입 스킬발동" + String(mouth_skill_count) + "번!");
      count2++;
      mouth_skill_count++;
    }
  }, 100); // 현재 0.1초
});
