input_string = """I have an opportunity named %Opportunity:OpportunityName% at the company called %Opportunity:AccountName%.
I expect the deal to close for $%Opportunity:ExpectedRevenue% in %Opportunity:DaysToClose% days.
I have a %Opportunity:Probability% percent chance of closing it.
It is in the %Opportunity:Stage% stage.

%StringOfContacts%

Please recommend 5 to 10 ideas I could try to move this deal along faster."""

input_string_array = input_string.split("\n")
output_string = '"' + "\\n".join(input_string_array) + '"'

print(output_string)

