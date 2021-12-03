function doneTyping() {
    document.getElementById("logo").style.marginTop = "0px"; 
    document.getElementById("companies_table").style.opacity = "0";
    document.getElementById("error").style.opacity = "0";

    setTimeout( () => {

        let name = document.getElementById('searchbar').value;     
        if (name == "") {
            return;
        }         

        fetch('http://localhost:8983/solr/companies/select?indent=true&q.op=OR&q=name%3A' + name + '*&rows=100&sort=rating%20desc')
        .then(response => response.json())
        .then(data => {

            if (data.response.docs.length == 0) {

                document.getElementById("error").style.marginTop = "100px";
                document.getElementById("companies_table").innerHTML = "";
                document.getElementById("error").innerHTML = "No companies were found."; 
                document.getElementById("error").style.opacity = "100";

            } else {    

                document.getElementById("error").style.marginTop = "0";
                document.getElementById("error").innerHTML = "";
                document.getElementById("companies_table").innerHTML = 
                    '<table id="companies"> \
                        <thead> \
                            <tr> \
                                <th> Companies </th> \
                                <th> Rating </th> \
                                <th> Country </th> \
                                <th> Size </th> \
                                <th> Industry </th> \
                            </tr> \
                        </thead> \
                        <tbody> \
                        </tbody> \
                    </table>';      
                document.getElementById("companies_table").style.opacity = "100";

                data.response.docs.forEach(company => {
                    
                    let table_row = document.getElementById('companies').insertRow();
                    
                    let url = document.createElement('a'); 
                    url.appendChild(document.createTextNode(company.name)); 
                    url.href = company.url;
                    url.target = "_blank";

                    let name_cell = table_row.insertCell();
                    name_cell.appendChild(url);

                    let rating_cell = table_row.insertCell();
                    rating_cell.appendChild(typeof company.rating !== 'undefined' ? document.createTextNode(company.rating) : document.createTextNode('N/A'));

                    let country_cell = table_row.insertCell();
                    country_cell.appendChild(document.createTextNode(company.country));   
                    
                    let size_cell = table_row.insertCell();
                    size_cell.appendChild(typeof company.size !== 'undefined' ? document.createTextNode(company.size) : document.createTextNode('N/A'));

                    let industry_cell = table_row.insertCell();
                    industry_cell.appendChild(typeof company.industry !== 'undefined' ? document.createTextNode(company.industry) : document.createTextNode('N/A'));   
                });
            }
        });
    }, 600);
}