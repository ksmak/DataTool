import { useTranslation } from "react-i18next"
import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";
import { useAuth } from "../../../lib/auth";

export default function LoginPage() {
    const navigate = useNavigate();
    const location = useLocation();
    const [database, setDatabase] = useState('')
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { t } = useTranslation();
    const { login } = useAuth();

    let fromPage = location.state?.from?.pathname || '/';

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        axios.post(`${process.env.REACT_APP_HOST_API}/api/token/`, { username: username, password: password })
            .then(resp => {
                login(resp.data.user, resp.data.access, resp.data.refresh);
                navigate(fromPage, { replace: true });
            })
            .catch(err => {
                if (err.response?.status === 401) {
                    setError(t('login_error'))
                } else {
                    setError(err.message)
                }
            })
    }
    return (
        <div className="mx-auto my-20 flex flex-col border-2 border-primary rounded-md p-5 w-80 bg-orange-50">
            <div className="font-bold text-lg text-center mb-4">
                {t('enter_in_system')}
            </div>
            <form onSubmit={handleSubmit}>
                <fieldset className="mb-4">
                    <label
                        className="font-bold text-sm block"
                        htmlFor="database"
                    >
                        {t('database')}
                    </label>
                    <select
                        className="text-sm border-2 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary p-1 rounded-md w-full"
                        id="database"
                        onChange={(e) => setDatabase(e.target.value)}
                    >

                    </select>
                </fieldset>
                <fieldset className="mb-4">
                    <label
                        className="font-bold text-sm block"
                        htmlFor="username"
                    >
                        {t('username')}
                    </label>
                    <input
                        className="text-sm border-2 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary p-1 rounded-md w-full"
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
                        className="text-sm border-2 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary p-1 rounded-md w-full"
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
                        className="bg-primary text-white p-2 mt-4 rounded-md w-fit"
                        type="submit"
                        value={t('enter')}
                    />
                </div>
            </form>
        </div>
    )
}