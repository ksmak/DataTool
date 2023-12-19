import { createContext, useContext, useEffect, useState } from "react";
import { IDatabase, IMetaContext } from "../types/types";
import api from "../api";

const MetaContext = createContext<IMetaContext>({
    db: null,
    setDb: null,
});

export function useMeta() {
    return useContext(MetaContext);
}

export function MetaProvider({ children }: any) {
    const [db, setDb] = useState<IDatabase | null>(null);

    useEffect(() => {
        api.datatool.getStructDb(1)
            .then(resp => {
                setDb(resp.data);
            })
            .catch(err => {
                console.log(err.message);
            })
    }, []);

    const meta = {
        db,
        setDb
    }

    return (
        <MetaContext.Provider value={meta}>
            {children}
        </MetaContext.Provider>
    )
}