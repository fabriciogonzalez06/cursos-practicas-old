using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
   public class Login
    {

        //propiedades

        public string usuario { get; set; }
        public string password { get; set; }

        //mensaje de error
        public  void MensajeErrror(string error)
        {
            MessageBox.Show(error, "Sistema Matricula", MessageBoxButtons.OK,MessageBoxIcon.Error);
        }

        //mensaje correcto
        public void correcto(string mensaje)
        {
            MessageBox.Show(mensaje, "Sistema Matricula", MessageBoxButtons.OK,MessageBoxIcon.Information);
        }


        //verificar que esten las contraseñas y password
        public bool verificar(ErrorProvider error,TextBox usuario,TextBox pass)
        {
            bool ok = true;

            if (usuario.Text=="" )
            {
                ok = false;
                error.SetError(usuario,"Ingrese el usuario por favor!!");
            }
            else
            {
                error.SetError(usuario,"");
            }

            if (pass.Text=="")
            {
                ok = false;
                error.SetError(pass,"Ingrese la contraseña por favor!!");
            }
            else
            {
                error.SetError(pass,"");
            }

            return ok;
        }
    


    }
}
