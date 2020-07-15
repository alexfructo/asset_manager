
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
                "localizacao": function () { return $('#unidade').val() },
                "setor": function () { return $('#setor').val() },
                "grupo": function () { return $('#localizacao').val() },
                "categoria": function () { return $('#equipamento').val() },
                "fabricante": function () { return $('#fabricante').val() },
                "status": function () { return $('#status').val() },
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
                    return `<a href="/equipamento/editar/${data}" class="btn btn-icon btn-pill btn-primary btn-sm" data-toggle="tooltip" title="Editar"><i class="fa fa-fw fa-edit"></i> </a> <a href="/equipamento/remover/${data}" class="btn btn-icon btn-pill btn-danger btn-sm" data-toggle="tooltip" title="Remover"> <i class="fa fa-fw fa-trash"></i></a>`;
                }
            },
        ],
    });
}