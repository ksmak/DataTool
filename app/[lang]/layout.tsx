import type { Metadata } from 'next';
import './globals.css';
import { i18n } from '../../i18n-config'
import Navigator from './components/navigator';

export async function generateStaticParams() {
  return i18n.locales.map((locale) => ({ lang: locale }))
}

export const metadata: Metadata = {
  title: 'DataTool',
}

export default function RootLayout({
  children,
  params,
}: {
  children: React.ReactNode,
  params: { lang: string }
}) {
  return (
    <html lang={params.lang}>
      <body>
        <Navigator lang={params.lang} />
        {children}
      </body>
    </html>
  )
}
