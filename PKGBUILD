# Maintainer: Kwpolska <kwpolska@kwpolska.tk>
pkgname=trashman
pkgver=0.2.0
pkgrel=1
pkgdesc='A Python XDG trash manager. (built under py3k)'
arch=('any')
url='https://github.com/Kwpolska/pkgbuilder'
license=('BSD')
depends=('python')
options=(!emptydirs)
source=("http://pypi.python.org/packages/source/t/${pkgname}/${pkgname}-${pkgver}.tar.gz")
md5sums=('acb9613c9db9585ca88c5efbd5706207')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
