function communitySize(result, i) {
  return result[i]['screen_names'].length;
}
var community1Size = communitySize({{ community1|safe }},1)
var community2Size = communitySize({{ community1|safe }},2)
var community3Size = communitySize({{ community1|safe }},3)
var community4Size = communitySize({{ community1|safe }},4)


var words = [
              {text: "Lorem", weight: 13},
              {text: "Ipsum", weight: 10.5},
              {text: "Dolor", weight: 9.4},
              {text: "Sit", weight: 8},
              {text: "Amet", weight: 6.2},
              {text: "Consectetur", weight: 5},
              {text: "Adipiscing", weight: 5},
              {text: "Test", weight: 13},
              {text: "Michel", weight: 2},
              {text: "Albert", weight: 24}
                                ];
$('#keywords').jQCloud(words);
$('#keywordsa').jQCloud(words);
$('#keywordsb').jQCloud(words);
$('#keywordsc').jQCloud(words);
