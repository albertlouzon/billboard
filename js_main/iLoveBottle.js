$('document').ready(function () {
    $('#getList').on('click', function(){
        showUserList()
        getLastVisited()
    });
    $('#reload').on('click', reloadPage);
});


getLastVisited = function () {
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/getLastUpdated",

        success: function (lastUpdated) {
            $('#cookie').empty()
            var newDiv = $("<span>");
            newDiv.text("last update of the headlines : "+ lastUpdated)
            $('#cookie').append(newDiv);
        },
        error: function (lastUpdated) {
            alert("Request failed with message : " + msg);
        }
    });
}

showUserList = function () {
    $('#userList').empty();
    $.ajax({
        type: "GET",
        dataType: 'json',
        url: "http://localhost:7000/rss_dict",

        success: function (list0) {
            for (var i = 0; i < list0.length; i++) {
                var newDiv = $("<pre>");
                var newHref = $("<a>");
                newHref.text(list0[i].title)
                newHref.attr('href', list0[i].link)
                newDiv.append(newHref)
                $('.userList').append(newDiv);

            }
        },
        error: function (list0) {
            alert("Request failed with message : " + list0);
        }
    });

}


reloadPage = function(){
    $('.userList').empty()
    $('#cookie').empty()
    showUserList()
}