import { useTranslation } from "react-i18next"
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";
import { useAuth } from "../../../lib/auth";
import api from "../../../api";
import { useMeta } from "../../../lib/meta";
import Language from "../elements/Language";

export default function LoginPage() {
    const navigate = useNavigate();
    const location = useLocation();
    const [database, setDatabase] = useState(0);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { t } = useTranslation();
    const { login, dbList } = useAuth();
    const { setDb } = useMeta();

    useEffect(() => {
        setDatabase(Number(localStorage.getItem('db')));
    }, []);

    let fromPage = location.state?.from?.pathname || '/';

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        axios.post(`${process.env.REACT_APP_HOST_API}api/token/`, { username: username, password: password })
            .then(resp => {
                const user = resp.data.user;
                const accessToken = resp.data.access;
                const refreshToken = resp.data.refresh;
                api.datatool.getDb(database, accessToken)
                    .then(resp => {
                        setDb(resp.data);
                        login(user, accessToken, refreshToken);
                        navigate(fromPage, { replace: true });
                    })
                    .catch(err => {
                        if (err.response?.status === 404) {
                            setError(t('access_error'))
                        } else {
                            setError(err.message)
                        }
                    })
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
        <div className="mx-auto my-20 flex flex-col border-2 border-yellow rounded-md p-5 w-80 bg-primary">
            <Language />
            <div className="text-white font-bold text-lg text-center mb-4 mt-4">
                {t('enter_in_system')}
            </div>
            <form onSubmit={handleSubmit}>
                <fieldset className="mb-4">
                    <label
                        className="text-white font-bold text-sm block"
                        htmlFor="database"
                    >
                        {t('database')}
                    </label>
                    <select
                        className="text-sm border-2 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary p-1 rounded-md w-full"
                        id="database"
                        onChange={(e) => setDatabase(Number(e.target.value))}
                        value={database}
                    >
                        <option value={0}></option>
                        {dbList.map(db => (<option key={db.id} value={db.id}>{db.title}</option>))}
                    </select>
                </fieldset>
                <fieldset className="mb-4">
                    <label
                        className="text-white font-bold text-sm block"
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
                        className="text-white font-bold text-sm block"
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
                        className="bg-primary text-white p-2 mt-4 rounded-md w-fit border-2 border-white hover:cursor-pointer"
                        type="submit"
                        value={t('enter')}
                    />
                </div>
            </form>
        </div>
    )
}