import { createContext, useContext, useState } from "react";
import { IDatabase, IMetaContext } from "../types/types";

const MetaContext = createContext<IMetaContext>({
    database: null,
    setDb: (db: IDatabase) => { }
});

export function useMeta() {
    return useContext(MetaContext);
}

export function MetaProvider({ children }: any) {
    const [database, setDatabase] = useState<IDatabase | null>(null);

    function setDb(db: IDatabase) {
        setDatabase(db);
        localStorage.setItem('db', String(db.id));
    }

    const meta = {
        database,
        setDb
    }

    return (
        <MetaContext.Provider value={meta}>
            {children}
        </MetaContext.Provider>
    )
}