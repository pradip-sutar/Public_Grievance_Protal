$(document).ready(function() {
    let $id_sub_category = $("#id_sub_category");
    let $submit_grievance = $(".submit_grievance");
    let $id_category = $("#id_category");

    function get_subcategories() {
        let url = $(".form-loads-subcategories").data("sub-categories-url");
        let category = $id_category.val();

        console.log("Requesting subcategories from:", url);
        console.log("Category ID:", category);

        $.ajax({
            url: url,
            data: {
                'category': category
            },
            beforeSend: function() {
                $id_sub_category.html('<option>Loading...</option>');
                $id_sub_category.attr("disabled", true);
                $submit_grievance.attr("disabled", true);
            },
            success: function(data) {
                console.log("Subcategories data:", data);

                if (data.dept_categories && data.dept_categories.length > 0) {
                    $id_sub_category.html('');
                    $.each(data.dept_categories, function(index, item) {
                        $id_sub_category.append($('<option>', {
                            value: item.id,
                            text: item.name
                        }));
                    });
                    $id_sub_category.removeAttr("disabled");
                    $submit_grievance.removeAttr("disabled");
                } else {
                    $id_sub_category.html('<option>No sub-categories available</option>');
                    $id_sub_category.attr("disabled", true);
                    $submit_grievance.attr("disabled", true);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error("Error occurred:", textStatus, errorThrown);
                $id_sub_category.html('<option>Error loading sub-categories</option>');
                $id_sub_category.attr("disabled", true);
                $submit_grievance.attr("disabled", true);
            }
        });
    }

    if ($id_category.length) {
        $id_category.change(function() {
            get_subcategories();
        });

        // Trigger change event if category is preselected
        if ($id_category.val()) {
            get_subcategories();
        }
    }
});
