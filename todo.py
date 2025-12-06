import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """JSON dosyasını okur, görevleri liste olarak döner."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    """Görev listesini JSON dosyasına kaydeder."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task():
    """Yeni görev ekler."""
    title = input("Görev adı: ")
    task = {"title": title, "completed": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Görev eklendi.")

def list_tasks():
    """Tüm görevleri listeler."""
    tasks = load_tasks()
    if not tasks:
        print("Henüz görev yok 🙂")
        return

    print("\n📋 Görev Listesi:")
    print("-" * 30)
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['title']}   [{status}]")
    print("-" * 30)

def complete_task():
    """Bir görevi tamamlandı olarak işaretler."""
    tasks = load_tasks()
    list_tasks()

    if not tasks:
        return

    try:
        idx = int(input("Tamamlanan görev numarası: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            save_tasks(tasks)
            print("🎉 Görev tamamlandı!")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen sayısal bir değer gir.")

def delete_task():
    """Bir görevi siler."""
    tasks = load_tasks()
    list_tasks()

    if not tasks:
        return

    try:
        idx = int(input("Silmek istediğin görev numarası: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"🗑️ '{removed['title']}' silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen sayısal bir değer gir.")

def show_menu():
    print("\n===== DBB TO-DO APP =====")
    print("1) Görevleri Listele")
    print("2) Görev Ekle")
    print("3) Görevi Tamamlandı Olarak İşaretle")
    print("4) Görevi Sil")
    print("5) Çıkış")
    print("==========================")

def main():
    while True:
        show_menu()
        choice = input("Seçimin: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Görüşürüz 👋")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
