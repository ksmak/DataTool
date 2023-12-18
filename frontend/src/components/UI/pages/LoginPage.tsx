import { useTranslation } from "react-i18next"
import api from "../../../api"
import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { setCookie } from "../../../utils/cookies";

export default function LoginPage() {
    const navigate = useNavigate();
    const location = useLocation();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { t } = useTranslation();
    let fromPage = location.state?.from?.pathname || '/';
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        api.datatool.login(
            username, password
        ).then(resp => {
            const access_msc = process.env.REACT_APP_ACCESS_TOKEN_LIFETIME
                ? parseInt(process.env.REACT_APP_ACCESS_TOKEN_LIFETIME)
                : 10800000 //defult
            setCookie('access_token', resp.data.access, access_msc)
            const refresh_msc = process.env.REACT_APP_REFRESH_TOKEN_LIFETIME
                ? parseInt(process.env.REACT_APP_REFRESH_TOKEN_LIFETIME)
                : 86400000 //default
            setCookie('refresh_token', resp.data.refresh, refresh_msc)
            setCookie('username', resp.data.full_name, refresh_msc)
            navigate(fromPage, { replace: true })
        })
            .catch(err => {
                if (err.response?.status === 401) {
                    setError(t('error_login'))
                } else {
                    setError(err.message)
                }
            })
    }
    return (
        <div className="mx-auto my-20 flex flex-col border-2 border-orange-800 rounded-md p-5 w-80 bg-orange-50">
            <div className="font-bold text-lg text-center mb-4">
                {t('enter_in_system')}
            </div>
            <form onSubmit={handleSubmit}>
                <fieldset className="mb-4">
                    <label
                        className="font-bold text-sm block"
                        htmlFor="username"
                    >
                        {t('username')}
                    </label>
                    <input
                        className="text-sm border-2 focus:outline-none focus:border-orange-800 focus:ring-1 focus:ring-orange-800 p-1 rounded-md w-full"
                        id="username"
                        type="text"
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </fieldset>
                <fieldset>
                    <label
                        className="font-bold text-sm block"
                        htmlFor="password"
                    >
                        {t('password')}
                    </label>
                    <input
                        className="text-sm border-2 focus:outline-none focus:border-orange-800 focus:ring-1 focus:ring-orange-800 p-1 rounded-md w-full"
                        id="password"
                        type="password"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </fieldset>
                <div className='flex flex-row justify-center p-2 mb-4'>
                    <div className="h-4 text-red-600 text-sm">
                        {error}
                    </div>
                </div>
                <div
                    className="flex flex-col items-center"
                >
                    <input
                        className="bg-orange-800 text-white p-2 mt-4 rounded-md w-fit"
                        type="submit"
                        value={t('enter')}
                    />
                </div>
            </form>
        </div>
    )
}