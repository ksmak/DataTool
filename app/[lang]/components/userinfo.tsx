export default function UserInfo() {
    return (
        <div className="flex flex-col justify-center items-center text-sm text-white">
            <div>
                Пользователь
            </div>
            <div className="flex flex-row justify-center gap-2 lowercase">
                <div>
                    Профиль
                </div>
                <div>
                    Выход
                </div>
            </div>
        </div>
    )
}