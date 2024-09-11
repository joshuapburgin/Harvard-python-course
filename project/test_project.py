from project import Company,sorting_customer_objects
import unittest
from project import Employee
from project import input_openai, targeted_company

import pytest

emp=Employee(10,2,"josh","josh@gmail.com","https://www.linkedin.com/in/valid-profile/", "sales director")

#unit test to test that the email is in the right format
def test_email():
    with pytest.raises(ValueError, match="Email not in correct format"):
        emp.email= "john email"
#unit test to test that the linkedin url is the correct format
def test_linkedin():
    with pytest.raises(ValueError, match="Linkedin link not in correct format"):
        emp.linkedin= "john linkedin"
#unit test to test output from the openAI model is correct
def test_openai_input():
    actual_number_of_employees, actual_industry = input_openai("retail and 5 employees")

    assert actual_number_of_employees== 5
    assert actual_industry=='"retail"'
#unit test to ensure that output from MongdB is correct when taking into account company preferences
def test_finding_ideal_company():
    expected_output = (
        "Company: openai\n"
        "\tEmployee Name: Evan Shankman\tEmail: evanshanky@openai.com\n"
        "\tEmployee Name: Ben Julian\tEmail: benjuls@king.com\n"
        "\tEmployee Name: Sam Altman\tEmail: sam@openai.com"
    )
    assert targeted_company(1, "technology") == expected_output
#unit test to ensure that the sorting function works correctly for company objects
def test_sorting_customer_objects():
    # Sample data
    company1 = Company(1, "Apple", "https://www.apple.com/", "Technology")
    company2 = Company(2, "Google", "https://www.google.com/", "Technology")
    company3 = Company(3, "Microsoft", "https://www.microsoft.com/", "Technology")
    company4 = Company(4, "Amazon", "https://www.amazon.com/", "E-Commerce")

    many_companies = [company3, company1, company4, company2]

    # Expected order after sorting
    expected_sorted_companies = [company4, company1, company2, company3]

    # Call the function
    sorted_companies = sorting_customer_objects(many_companies)

    # Print the actual sorted company names for debugging
    print("Sorted companies:", [company.name for company in sorted_companies])

    # Assertions
    for sorted_company, expected_company in zip(sorted_companies, expected_sorted_companies):
        assert sorted_company.name == expected_company.name
        assert sorted_company.companyID == expected_company.companyID
        assert sorted_company.website == expected_company.website
        assert sorted_company.industry == expected_company.industry

    print("All tests passed for test_sorting_customer_objects")


