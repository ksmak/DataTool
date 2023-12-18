import React, { useContext } from 'react'
import { useLocation, Navigate } from 'react-router-dom'
import { getCookie } from '../../utils/cookies'
import { AuthContext } from '../../App'

interface Props {
    children?: any
}

export default function ProtectedRoute(props: Props) {
    const { accessToken } = useContext(AuthContext)
    const location = useLocation();


    if (!accessToken && getCookie('access_token') !== accessToken) {
        return <Navigate to="/login" replace state={{ from: location }} />
    }

    return props.children
}