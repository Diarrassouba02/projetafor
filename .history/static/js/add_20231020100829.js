var counter = 1;
function add_more() {
    counter++
    var newDiv = `<div id="product_row${counter}" class="row">
                    <div class="col-md-4">
                        <label>Nom</label>
                        <input id="name${counter}" type="text" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>Prénom</label>
                        <input id="price${counter}" type="text" class="form-control">
                    </div>
                    <div class="col-md-4">
                        <label>Prénom</label>
                        <input id="price${counter}" type="date" class="form-control">
                    </div>
                    <div class="col-md-1">
                        <br>
                        <button onclick="delete_row('${counter}')" type="button" class="btn btn-danger">Delete</button>
                    </div>
                </div>`
    var form = document.getElementById('input-form')
    form.insertAdjacentHTML('beforeend', newDiv);
}

function delete_row(id) {
    document.getElementById('product_row'+id).remove()
}

