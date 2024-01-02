import { createContext, useContext, useEffect, useState } from "react";
import { IAuthContext, IDb, IUser } from "../types/types";
import { setCookie } from "../utils/cookies";
import { Navigate, useLocation } from "react-router-dom";
import api from "../api";

const AuthContext = createContext<IAuthContext>({
    user: null,
    isAuthenticated: false,
    login: (user: IUser, accessToken: string, refreshToken: string) => { },
    logout: () => { },
    dbList: [],
});

export function useAuth() {
    return useContext(AuthContext);
}

export function AuthProvider({ children }: any) {
    const [user, setUser] = useState<IUser | null>(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [dbList, setDbList] = useState<IDb[]>([]);

    useEffect(() => {
        getDbList();
    })

    async function getDbList() {
        api.datatool.getDbList()
            .then(resp => {
                setDbList(resp.data);
            })
            .catch(err => {
                console.log(err.message);
            })
    }

    function login(user: IUser, accessToken: string, refreshToken: string) {
        setIsAuthenticated(true);
        setUser(user);
        const access_msc = process.env.REACT_APP_ACCESS_TOKEN_LIFETIME
            ? parseInt(process.env.REACT_APP_ACCESS_TOKEN_LIFETIME)
            : 10800000; //defult
        setCookie('access_token', accessToken, access_msc)
        const refresh_msc = process.env.REACT_APP_REFRESH_TOKEN_LIFETIME
            ? parseInt(process.env.REACT_APP_REFRESH_TOKEN_LIFETIME)
            : 86400000; //default
        setCookie('refresh_token', refreshToken, refresh_msc);
    }

    const logout = () => {
        setIsAuthenticated(false);
        setUser(null);
        setCookie('access_token', '', 0);
        setCookie('refresh_token', '', 0);
    }

    const auth: IAuthContext = {
        user,
        isAuthenticated,
        login,
        logout,
        dbList,
    }

    return (
        <AuthContext.Provider value={auth}>
            {children}
        </AuthContext.Provider>
    )
}

export function ProtectedRouter({ children }: any) {
    const { isAuthenticated } = useAuth();
    const location = useLocation();

    if (!isAuthenticated) {
        return <Navigate to="/login" replace state={{ from: location }} />;
    }

    return children;
}

