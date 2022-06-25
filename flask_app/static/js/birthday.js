let month_values = document.querySelectorAll("#pendingMonth")
let day_values = document.querySelectorAll("#pendingDay")
let birthday_month_values = document.querySelectorAll("#birthdayMonth")
let birthday_values = document.querySelectorAll("#birthDay")

let my_rows = document.querySelectorAll("#birthdayRow")

for (let i = 0; i < my_rows.length; i++) {
    let birthday_data = my_rows[i].childNodes[3].childNodes[1].innerHTML

    let d = new Date(birthday_data);

    let birthdayMonth = d.getMonth() + 1;
    let birthdayDay = d.getDate() + 1;


    let currentDate = new Date();


    if ((currentDate.getMonth() + 1) === birthdayMonth && (currentDate.getDate()) === birthdayDay ){
        my_rows[i].style.backgroundColor = '#3ED625';
    } else if ((currentDate.getMonth() + 1) === birthdayMonth) {
        my_rows[i].style.backgroundColor = '#F9F018';
    }
}





function convertDate(ids, convertTo) {
    for (let i = 0; i < ids.length; i++) {
        let value = ids[i].innerHTML;
        let d = new Date(value);

        if (convertTo === "day") {
            let conversion = d.getDate(value)+1;
            ids[i].innerHTML = conversion;
        } else if (convertTo === "month") {
            let conversion = d.getMonth(value)+1;
            ids[i].innerHTML = conversion;
        }

    }
}



convertDate(month_values, "month")
convertDate(day_values, "day")
convertDate(birthday_month_values, "month")
convertDate(birthday_values, "day")