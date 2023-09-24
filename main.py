import datetime
import os


def generate_folders(start_date, end_date, base_dir):
    """Generates a hierarchy of folders from start_date to end_date, starting with a year folder, then year-month
    folders, and finally day folders.

  Args:
    start_date: A datetime.date object representing the start date.
    end_date: A datetime.date object representing the end date.
    base_dir: The base directory where the folders will be created.
  """

    while start_date <= end_date:
        year_folder = os.path.join(base_dir, str(start_date.year))
        year_month_folder = os.path.join(year_folder, f"{start_date.year}-{start_date.month:02d}")
        year_month_day_folder = os.path.join(year_month_folder,
                                             f"{start_date.year}-{start_date.month:02d}-{start_date.day:02d}")
        # day_folder = os.path.join(year_month_folder, str(start_date.day).zfill(2))

        # Create the folders if they don't exist.
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)
        if not os.path.exists(year_month_folder):
            os.makedirs(year_month_folder)
        if not os.path.exists(year_month_day_folder):
            os.makedirs(year_month_day_folder)

        start_date += datetime.timedelta(days=1)


# Get the start and end dates.
my_start_date = datetime.date(2023, 1, 1)
my_end_date = datetime.date(2023, 12, 31)

# Create the folders.
generate_folders(my_start_date, my_end_date, "")
