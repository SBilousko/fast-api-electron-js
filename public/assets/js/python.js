const axios = require("axios").default;

const base_url = "http://127.0.0.1:7777/";

const options = {
  headers: {
    "Content-Type": "application/json",
  },
};

function createListItem(parent, child) {
  let li = document.createElement("li");
  li.innerHTML = child;
  parent.appendChild(li);
}

function splitString(stringToSplit, separator) {
  return (arrayOfStrings = stringToSplit.split(separator));
}

axios
  .get(base_url, options)
  .then((res) => {
    filesJSON = res.data;
    let ul = document.createElement("ul");
    for (let i = 0; i < filesJSON.length; i++) {
      createListItem(ul, filesJSON[i].name);
    }
    filesList.appendChild(ul);
    apiResult.innerHTML = JSON.stringify(res, null, 4);
  })
  .catch((err) => {
    apiResult.innerHTML = JSON.stringify(err, null, 4);
  });

function add_file() {
  let file_path = inputFilePath.value;
  let file_name = splitString(file_path, "\\").find(
    (element) => element.indexOf(".") != -1
  );
  let endpoint = base_url + "file_path/";
  let req_data = {
    name: file_name,
    path: file_path,
  };

  axios
    .post(endpoint, req_data, options)
    .then((res) => {
      console.log("file path: ", file_path);
      apiResult.innerHTML = JSON.stringify(res, null, 4);
    })
    .catch((err) => {
      apiResult.innerHTML = JSON.stringify(err, null, 4);
    });
}

function clearDB() {
  // axios
  // .get(base_url + "delete/", options)
  // .then((res) => {
  //   filesJSON = res.data;
  //   let ul = document.createElement("ul");
  //   for (let i = 0; i < filesJSON.length; i++) {
  //     createListItem(ul, filesJSON[i].name);
  //   }
  //   filesList.appendChild(ul);
  //   apiResult.innerHTML = JSON.stringify(res, null, 4);
  // })
  // .catch((err) => {
  //   apiResult.innerHTML = JSON.stringify(err, null, 4);
  // });
  axios
    .delete(base_url, options)
    .then((res) => {
      filesList.innerHTML = "Files deleted";
      apiResult.innerHTML = JSON.stringify(res, null, 4);
    })
    .catch((err) => {
      apiResult.innerHTML = JSON.stringify(err, null, 4);
    });
}
