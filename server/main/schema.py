from ma import ma
from models import MusicModel


class MusicSchema(ma.ModelSchema):
    class Meta:
        model = MusicModel
        # dump_only = ("id",)
        include_fk = True
        


music_schema = MusicSchema()