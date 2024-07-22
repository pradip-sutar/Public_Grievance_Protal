let $id_sub_category = $("#id_sub_category");
let $submit_grievance = $(".submit_grievance");
let $id_category = $("#id_category");

function get_subcategories() {
    let url = $(".form-loads-subcategories").data("sub-categories-url");
    let category = $id_category.val();
    $.ajax({
        url: url,
        data: {
            'category': category
        },
        success: function (data) {
            console.log(data); // Log data to verify the format
            if (data.dept_categories) {
                $id_sub_category.html('');
                $.each(data.dept_categories, function (index, item) {
                    $id_sub_category.append($('<option>', {
                        value: item.id,
                        text: item.name
                    }));
                });
                $id_sub_category.removeAttr("disabled");
                $submit_grievance.removeAttr("disabled");
            } else {
                $id_sub_category.html('');
                $id_sub_category.attr("disabled", true);
                $submit_grievance.attr("disabled", true);
            }
        },
        error: function () {
            $id_sub_category.html('');
            $id_sub_category.attr("disabled", true);
            $submit_grievance.attr("disabled", true);
        }
    });
}

$id_category.change(function () {
    get_subcategories();
});
