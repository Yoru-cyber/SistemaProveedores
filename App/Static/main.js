fetch("http://localhost:5000/Ventas")
  .then((response) => response.json())
  .then((data) => {
    const tbody = document.getElementById("tbody");
    data.forEach((element) => {
      const deleteButton = document.createElement("button");
      deleteButton.innerHTML = "Eliminar";
      deleteButton.className = "btn btn-danger";
      deleteButton.id = element.id;
      deleteButton.name = 'deleteBtn';
      const editButton = document.createElement("button");
      editButton.innerHTML = "Editar";
      editButton.className = "btn btn-secondary";
      editButton.name = 'editBtn';
      editButton.id = element.id;
      editButton.onclick = () => {
        window.location.href = `/Venta/${editButton.id}/edit`;
      }
      deleteButton.onclick = () => {
        window.location.href = `/Venta/${deleteButton.id}/delete`;
      }
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      const td4 = document.createElement("td");
      const td5 = document.createElement("td");
      const td6 = document.createElement("td");
      const td7 = document.createElement("td");
      td1.innerHTML = element.id;
      td2.innerHTML = element.nameProvider;
      td3.innerHTML = element.nameProduct;
      td4.innerHTML = element.unitsProduct;
      td5.innerHTML = element.pricePerUnit;
      td6.innerHTML = element.date;
      td7.appendChild(deleteButton);
      td7.appendChild(editButton);
      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tr.appendChild(td4);
      tr.appendChild(td5);
      tr.appendChild(td6);
      tr.appendChild(td7);
      tbody.appendChild(tr);
    });
  });
