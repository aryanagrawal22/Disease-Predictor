const express = require("express");
const https = require("https");
const { dirname } = require("path");
const bodyParser = require("body-parser");
const { request } = require("http");
const axios = require("axios");
const ejs = require("ejs");
const fs = require('fs')

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", function (req, res) {
  res.render("home");
});

app.get("/heart_result", function (req, res) {
  res.render("heart_result");
});

app.get("/stroke_result", function (req, res) {
  res.render("stroke_result");
});

app.get("/hepatitis_result", function (req, res) {
  res.render("hepatitis_result");
});

app.get("/heart_prediction", function (req, res) {
  res.render("heart_disease_predictor");
});

app.post("/heart_prediction", function (req, res) {
  const {
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal,
  } = req.body;
  var sexVal, cpVal, fbsVal, restecgVal, exangVal, slopeVal, thalVal;
  if (sex == "Male") {
    sexVal = 1;
  } else {
    sexVal = 0;
  }
  if (cp == "Typical Angina") {
    cpVal = 0;
  } else if (cp == "Atypical Angina") {
    cpVal = 1;
  } else if (cp == "Non-Anginal Pain") {
    cpVal = 2;
  } else {
    cpVal = 3;
  }
  if (fbs == "Yes") {
    fbsVal = 1;
  } else {
    fbsVal = 0;
  }
  if (restecg == "Normal") {
    restecgVal = 0;
  } else if (restecg == "ST-T wave abnormality") {
    restecgVal = 1;
  } else {
    restecgVal = 2;
  }
  if (exang == "Yes") {
    exangVal = 1;
  } else {
    exangVal = 0;
  }
  if (slope == "Upsloping") {
    slopeVal = 0;
  } else if (slope == "Flat") {
    slopeVal = 1;
  } else {
    slopeVal = 2;
  }
  if (thal == "Normal") {
    thalVal = 1;
  } else if (thal == "Fixed Defect") {
    thalVal = 2;
  } else {
    thalVal = 3;
  }

  axios
    .post("https://disease-predict-api.herokuapp.com/predict_heart", {
      age: age,
      sex: sexVal,
      cp: cpVal,
      trestbps: trestbps,
      chol: chol,
      fbs: fbsVal,
      restecg: restecgVal,
      thalach: thalach,
      exang: exangVal,
      oldpeak: oldpeak,
      slope: slopeVal,
      ca: ca,
      thal: thalVal,
    })
    .then((result) => {
      var message, sub_message;
      var imageEncoded = result.data.image;
      let buff = new Buffer(imageEncoded, 'base64');
      fs.writeFileSync('./public/images/output.png', buff);
      if (result.data.prediction == 0) {
        message = "You've not been diagnosed with any Heart Disease.";
        sub_message = "Cheer up!";
      } else {
        message = "You've been diagnosed with Heart Disease.";
        sub_message = "Please consult your doctor at earliest.";
      }
      res.render("heart_result", {
        message: message,
        sub_message: sub_message,
      });
    })
    .catch((error) => {
      console.error(error);
    });
});

app.get("/stroke_prediction", function (req, res) {
  res.render("stroke_predictor");
});

app.post("/stroke_prediction", function (req, res) {
  const {
    gender,
    age,
    hypertension,
    heart_disease,
    ever_married,
    work_type,
    Residence_type,
    avg_glucose_level,
    bmi,
    smoking_status,
  } = req.body;
  var genderVal,
    hypertensionVal,
    heartVal,
    marriedVal,
    workVal,
    residenceVal,
    smokingVal;

  if (gender == "Male") {
    genderVal = 1;
  } else {
    genderVal = 0;
  }

  if (hypertension == "Yes") {
    hypertensionVal = 1;
  } else {
    hypertensionVal = 0;
  }

  if (heart_disease == "Yes") {
    heartVal = 1;
  } else {
    heartVal = 0;
  }

  if (ever_married == "Yes") {
    marriedVal = 1;
  } else {
    marriedVal = 0;
  }

  if (work_type == "Private") {
    workVal = 0;
  } else if (work_type == "Self-Employed") {
    workVal = 1;
  } else if (work_type == "Government-Job") {
    workVal = 2;
  } else {
    workVal = 3;
  }

  if (Residence_type == "Urban") {
    residenceVal = 1;
  } else {
    residenceVal = 0;
  }

  if (smoking_status == "Never Smoked") {
    smokingVal = 0;
  } else if (smoking_status == "Formerly Smoked") {
    smokingVal = 1;
  } else {
    smokingVal = 2;
  }

  axios
    .post("https://disease-predict-api.herokuapp.com/predict_stroke", {
      gender: genderVal,
      age: age,
      hypertension: hypertensionVal,
      heart_disease: heartVal,
      ever_married: marriedVal,
      work_type: workVal,
      Residence_type: residenceVal,
      avg_glucose_level: avg_glucose_level,
      bmi: bmi,
      smoking_status: smokingVal,
    })
    .then((result) => {
      var message, sub_message;
      var imageEncoded = result.data.image;
      let buff = new Buffer(imageEncoded, 'base64');
      fs.writeFileSync('./public/images/output.png', buff);
      if (result.data.prediction == 0) {
        message = "You do not have a chance of getting a Stroke.";
        sub_message = "Cheer up!";
      } else {
        message = "You've a chance of getting stroke.";
        sub_message = "Please consult your doctor at earliest.";
      }
      res.render("stroke_result", {
        message: message,
        sub_message: sub_message,
      });
    })
    .catch((error) => {
      console.error(error);
    });
});

app.get("/hepatitis_prediction", function (req, res) {
  res.render("hepatitis_predictor");
});

app.post("/hepatitis_prediction", function (req, res) {
  const { age, gender, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot } =
    req.body;
  var genderVal;
  if (gender == "Male") {
    genderVal = 1;
  } else {
    genderVal = 2;
  }

  axios
    .post("https://disease-predict-api.herokuapp.com/predict_hepatitis", {
      Age: age,
      Sex: genderVal,
      ALB: alb,
      ALP: alp,
      ALT: alt,
      AST: ast,
      BIL: bil,
      CHE: che,
      CHOL: chol,
      CREA: crea,
      GGT: ggt,
      PROT: prot,
    })
    .then((result) => {
      var message, sub_message;
      var imageEncoded = result.data.image;
      let buff = new Buffer(imageEncoded, 'base64');
      fs.writeFileSync('./public/images/output.png', buff);
      if (result.data.prediction == 0) {
        message = "You've not been diagnosed with Hepatitis.";
        sub_message = "Cheer up!";
      } else {
        message = "You've been diagnosed with Hepatitis.";
        sub_message = "Please consult your doctor at earliest.";
      }
      res.render("hepatitis_result", {
        message: message,
        sub_message: sub_message,
      });
    })
    .catch((error) => {
      console.error(error);
    });
});

app.listen(process.env.PORT || 3000 , function () {
  console.log("Server is running");
});
