# $UserList 

# $FirstName = "Franz"
# $LastName = "Ferdinand"
# $UserName = "Franz Ferdinand"
# $OU = "OU=Users,DC=contoso,DC=com"
# $City = "Springfield, OR"


# foreach ($User in $UserList) {

#      $Attributes = @{

#         Name = "$FirstName $LastName"
#         UserPrincipalName = "$FirstName.$LastName@GlobeXpower.com"
#         GivenName = $FirstName
#         Surname = $LastName
#         Company ="GlobeX"
#         Department = "TPS Department"
#         Title = "TSP Reporting Lead"
#         City = $City

#      }

#     New-ADUser @Attributes


    New-ADUser -Name "Franz Ferdinand" -Title "TSP Reporting Lead" -EmailAddress "ferdi@GlobeXpower.com" -company "GlobeX" -Department "TSP" -city "Springfield" -state "OR"
