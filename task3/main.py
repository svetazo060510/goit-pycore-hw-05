import sys
import collections
from pathlib import Path

def parse_log_line(line: str) -> dict:
    try:
        # Split the string into 4 parts: date, time, level, message
        date, time, level, message = line.split(' ', 3)
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message.strip()
        }
    except ValueError:
        # For cases where the string does not match the format
        print(f"Помилка: Некоректний формат логу: '{line.strip()}'")
        return None

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                log_detail = parse_log_line(line)
                if log_detail:
                    logs.append(log_detail)
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        sys.exit(1)       
    return logs

def count_logs_by_level(logs: list) -> dict:
    counts = collections.Counter(log['level'] for log in logs)
    return counts

def filter_logs_by_level(logs: list, level: str) -> list:
    level_lower = level.lower()
    return [log for log in logs if log['level'].lower() == level_lower]

def display_log_counts(counts: dict):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    # {<17} - left alignment, 17 characters
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

def main():
    # Check for at least one argument (file path)
    if len(sys.argv) < 2:
        print("Використання: python3 main.py /шлях/до/log_file.log [рівень_логування]")
        sys.exit(1)
    file_path = sys.argv[1]
    
    # Check for an optional second argument (logging level)
    log_level_to_filter = None
    if len(sys.argv) > 2:
        log_level_to_filter = sys.argv[2]

    # Load logs here
    logs = load_logs(file_path)
    
    if not logs:
        print("Лог-файл порожній або не містить коректних записів.")
        return

    # Calculate and display statistics
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Calculate and display statistics + for logging level
    if log_level_to_filter:
        filtered_logs = filter_logs_by_level(logs, log_level_to_filter)
        
        print(f"\nДеталі логів для рівня '{log_level_to_filter.upper()}':")
        if not filtered_logs:
            print("Записів для цього рівня не знайдено.")
        else:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()


