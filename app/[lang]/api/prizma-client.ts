import { PrismaClient } from '@prisma/client';
import { DictionaryType } from '../types/types';

const prisma = new PrismaClient();

async function getDictionaries() {
    const dictionaries = await prisma.dictionary.findMany();
    console.log(dictionaries)
}

export async function createDictionary(newDictionary: DictionaryType) {
    const dictionary = await prisma.dictionary.create({
        data: {
            name: newDictionary.name
        }
    })

    return dictionary;
}

async function getDatabases() {
    const databases = await prisma.database.findMany();
    console.log(databases)
}