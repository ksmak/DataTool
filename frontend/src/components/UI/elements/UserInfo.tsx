import { useTranslation } from "react-i18next"
import { useAuth } from "../../../lib/auth";

export default function UserInfo() {
    const { t } = useTranslation();
    const { user } = useAuth();

    return (
        <div className="flex flex-col justify-center items-center text-sm text-white">
            <div>
                {user?.fullName}
            </div>
            <div className="flex flex-row justify-center gap-2 lowercase">
                <div>
                    {t('profile')}
                </div>
                <div>
                    {t('exit')}
                </div>
            </div>
        </div>
    )
}