function saveFormData() {
    let formData = {};
        const formElements = document.getElementById('myForm').elements;

        for (let i = 0; i < formElements.length; i++) {
            const element = formElements[i];
            if (element.type !== 'button') {
                formData[element.name] = element.value;
            }
        }

        const json = JSON.stringify(formData, null, 2);
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = 'formData.json';
        a.click();

        URL.revokeObjectURL(url);
}


/*
      <label for="name">adjective:</label>
              <input type="text" id="adj1" name="adj1"><br><br>
              <label for="email">plural noun:</label>
              <input type="text" id="pnoun1" name="plu1"><br><br>
              <label for="email">adjective:</label>
              <input type="text" id="adj2" name="adj2"><br><br>
              <label for="email">plural noun:</label>
              <input type="text" id="pnoun2" name="plu2"><br><br>
              <label for="email">adjective:</label>
              <input type="text" id="adj3" name="adj3"><br><br>
              <label for="email">noun:</label>
              <input type="text" id="n1" name="noun1"><br><br>
              <label for="email">verb ending in ing:</label>
              <input type="text" id="verbing" name="vering"><br><br>
              <label for="email">noun:</label>
              <input type="text" id="n2" name="noun2"><br><br>


*/