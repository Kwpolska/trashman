# Maintainer: Kwpolska <kwpolska@kwpolska.tk>
pkgname=trashman
pkgver=0.1.2
pkgrel=1
pkgdesc='A Python XDG trash manager. (built under py3k)'
arch=('any')
url='https://github.com/Kwpolska/pkgbuilder'
license=('BSD')
depends=('python')
options=(!emptydirs)
source=("http://pypi.python.org/packages/source/t/${pkgname}/${pkgname}-${pkgver}.tar.gz")
md5sums=('e1502dff82eb6bbf6f31b29e9a2907b7')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
