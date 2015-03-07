# Maintainer: Chris Warrick <aur@chriswarrick.com>
pkgname=trashman
_pyname=trashman
pkgver=1.5.0
pkgrel=1
pkgdesc='A Python trash manager.'
arch=('any')
url='https://github.com/Kwpolska/trashman'
license=('BSD')
depends=('python')
options=(!emptydirs)
source=("http://pypi.python.org/packages/source/$(echo ${_pyname} | cut -c1)/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('761837310ac289fa9d596047b85466aa')

package() {
  cd "${srcdir}/${_pyname}-${pkgver}"
  python3 setup.py install --root="${pkgdir}/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
