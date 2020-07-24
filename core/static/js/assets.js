function getData() {
    return $('#assets').DataTable({
        "language": {
            "url": "http://cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json",
        },
        "processing": true,
        "responsive": true,
        "bLengthChange": false,
        "ajax": {
            "url": "/equipamentos/listar/json",
            "type": "GET",
            "data": {
                "localizacao": function () { return $('#localizacao_filtro').val() },
                "setor": function () { return $('#setor_filtro').val() },
                "grupo": function () { return $('#grupo_filtro').val() },
                "categoria": function () { return $('#categoria_filtro').val() },
                "fabricante": function () { return $('#fabricante_filtro').val() },
                "status": function () { return $('#status_filtro').val() },
            }
        },
        "columnDefs": [
            { "responsivePriority": 1, "targets": 0 },
            { "responsivePriority": 2, "targets": -1 }
        ],
        "columns": [
            { "data": "localizacao" },
            { "data": "setor" },
            { "data": "grupo" },
            { "data": "categoria" },
            { "data": "fabricante" },
            { "data": "modelo" },
            { "data": "numero_serie" },
            { "data": "numero_patrimonio" },
            { "data": "status" },
            {
                "data": "codigo",
                "render": function (data) {
                    return `<a data-id="${data}" href="/equipamento/editar/${data}" class="open-EditModal btn btn-icon btn-pill btn-primary btn-sm" data-toggle="modal" data-target="#editarModal"><i class="fa fa-fw fa-edit" data-toggle="tooltip" title="Editar"></i> </a> <a data-id="${data}" href="/equipamento/remover/${data}" class="open-EditModal btn btn-icon btn-pill btn-danger btn-sm"> <i class="fa fa-fw fa-trash" data-toggle="tooltip" title="Remover"></i></a>`;
                }
            },
        ],
    });
}

function cadastroSalvar() {
    $.ajax({
        url: "/equipamento/cadastro/ajax",
        type: "POST",
        data: {
            "csrfmiddlewaretoken": function () { return $("input[name=csrfmiddlewaretoken]").val() },
            "localizacao": function () { return $("#id_localizacao").val() },
            "setor": function () { return $("#id_setor").val() },
            "grupo": function () { return $("#id_grupo").val() },
            "categoria": function () { return $("#id_categoria").val() },
            "fabricante": function () { return $("#id_fabricante").val() },
            "status": function () { return $("#id_status").val() },
            "numero_serie": function () { return $("#id_numero_serie").val() },
            "numero_patrimonio": function () { return $("#id_numero_patrimonio").val() },
            "observacoes": function () { return $("#id_observacoes").val() },
        },
        beforeSend: function () {
            $("#cadastroSalvar").html('<i class="fa fa-spinner" aria-hidden="true"></i> Aguarde...');
            $('#cadastroSalvar').prop('disabled', true);
        },
        success: function (data) {
            if (data.success == true) {
                formCadastroLimpar();
                alert_class = "alert-success";
                alert_message = "Cadastro realizado com sucesso!";
            }
            else {
                alert_class = "alert-danger";
                alert_message = "Foram encontrados erros no formulário, por favor verifique as mensagens em vermelho.";

                if (data.message) {
                    for (property in data.message) {
                        $(`#${property}`).html("");
                        $(`#${property}`).append(`<div class="invalid-feedback d-block p-1 mt-2"><strong>${data.message[property]}</strong></div>`);
                    }
                }
            }
            $("#cadastroFormResult").html(`<div class="row justify-content-center align-items-center">
            <div class="col mb-3">
                <div class="alert ${alert_class} alert-dismissible text-center" role="alert">
                    <ul class='list-unstyled p-0 m-0'>
                        <li>${alert_message}</li>
                    </ul>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </div>
        </div>`);
        },
        error: function (xhr, errmsg, err) {
            console.warn(`${xhr.status}`);
            $("#cadastroFormResult").html(`<div class="row justify-content-center align-items-center">
            <div class="col mb-3">
                <div class="alert alert-danger alert-dismissible text-center" role="alert">
                    <ul class='list-unstyled p-0 m-0'>
                        <li>Não foi possível concluir a solicitação, por favor tente novamente.</li>
                    </ul>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </div>
        </div>`);
        },
        complete: function () {
            $("#cadastroSalvar").html("Salvar");
            $('#cadastroSalvar').prop('disabled', false);
            
        }
    });
}

function formCadastroLimpar() {
    $("#cadastroForm").trigger("reset");
    $("#id_localizacao").selectpicker("refresh");
    $("#id_setor").selectpicker("refresh");
    $("#id_grupo").selectpicker("refresh");
    $("#id_categoria").selectpicker("refresh");
    $("#id_fabricante").selectpicker("refresh");
    $("#id_status").selectpicker("refresh");
    $("#cadastroFormResult").html("");
    $("#localizacao").html("");
    $("#categoria").html("");
    $("#status").html("");
    $("#setor").html("");
    $("#grupo").html("");
    $("#fabricante").html("");
    $("#modelo").html("");
    $("#observacoes").html("");
    $("#numero_patrimonio").html("");
    $("#numero_serie").html("");
}

function formEditLoadData(id) {

    $.ajax(function(){

    });
}