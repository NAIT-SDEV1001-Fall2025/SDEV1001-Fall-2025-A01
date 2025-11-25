# some times you can rename imports for convenience so that
# you don't have to type as much
import pyexcel as pex

def create_game_reviews_excel_file(reviews, output_file):
    pex.save_as(array=reviews, dest_file_name=output_file)

def add_recommendation_column_to_excel_file(input_file, output_file):
    # load the existing excel file
    sheet = pex.get_sheet(file_name=input_file)

    # add a new column for recommendations based on score
    recommendations = ["Recommendation"]
    rows_list = sheet.to_array()
    for row_index, row_values in enumerate(rows_list[1:]):  # skip header
          # skip header row
        score = row_values[2] # this is the score column (0-based index)
        if score >= 90:
            recommendations.append("Highly Recommended")
        elif score >= 80:
            recommendations.append("Recommended")
        elif score >= 70:
            recommendations.append("Average")
        else:
            recommendations.append("Not Recommended")

    sheet.column += recommendations

    # save the updated sheet to a new file
    sheet.save_as(output_file)

def main():
    GAME_REVIEWS_FILE_NAME = "game_reviews.xlsx"
    GAME_REVIEWS = [
        ["Title", "Platform", "Score"],
        ["Elden Ring", "PC", 95],
        ["Stardew Valley", "Switch", 89],
        ["Cyberpunk 2077", "PS5", 82],
        ["No Man's Sky", "PC", 90],
        ["Gollum", "PS5", 43],
    ]
    # call our newly created function to create the excel file
    create_game_reviews_excel_file(GAME_REVIEWS, GAME_REVIEWS_FILE_NAME)
    print(f"Created {GAME_REVIEWS_FILE_NAME} with game reviews.")
    # now add the commended column in a new file.
    RECOMMENDED_GAME_REVIEWS_FILE_NAME = "recommended_game_reviews.xlsx"
    add_recommendation_column_to_excel_file(
        GAME_REVIEWS_FILE_NAME, RECOMMENDED_GAME_REVIEWS_FILE_NAME
    )
    print(f"Created {RECOMMENDED_GAME_REVIEWS_FILE_NAME} with recommendations.")

if __name__ == "__main__":
    main()