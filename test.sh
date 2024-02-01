REQUEST="{ \"firstNumber\": ${1-10}, \"secondNumber\": ${2-20} }"
echo Sending: "$REQUEST"
echo Response: 
curl -X POST -H "Content-Type: application/json" -d "$REQUEST" http://localhost:5000/add
