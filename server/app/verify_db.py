import sys
import traceback

with open("debug_log.txt", "w") as f:
    f.write("Script starting...\n")
    try:
        f.write("Importing os...\n")
        import os
        f.write("Importing database...\n")
        from database import engine
        f.write("Database imported.\n")

        def test_connection():
            f.write("Entering test_connection...\n")
            try:
                f.write(f"Url: {engine.url}\n")
                f.write("Connecting...\n")
                f.flush()
                with engine.connect() as connection:
                    f.write("Successfully connected!\n")
                return True
            except Exception as e:
                f.write(f"Exception: {e}\n")
                return False

        if __name__ == "__main__":
            f.write("Running main...\n")
            if test_connection():
                f.write("Success exit\n")
                sys.exit(0)
            else:
                f.write("Failure exit\n")
                sys.exit(1)
    except Exception as e:
        f.write(f"Top level exception: {e}\n")
        traceback.print_exc(file=f)
        sys.exit(1)
