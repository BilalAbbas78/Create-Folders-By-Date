import datetime
import os


def create_folders_by_date(start_date, end_date):
    """Creates folders with the format YYYYMMDD from the start date to the end date.

  Args:
    start_date: A datetime.date object representing the start date.
    end_date: A datetime.date object representing the end date.
  """

    for date in range(start_date.toordinal(), end_date.toordinal() + 1):
        folder_name = datetime.date.fromordinal(date).strftime("%Y%m%d")
        folder_path = os.path.join(os.getcwd(), "Folders/" + folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


if __name__ == "__main__":
    my_start_date = datetime.date.today()
    my_end_date = datetime.date(2023, 12, 31)

    create_folders_by_date(my_start_date, my_end_date)
